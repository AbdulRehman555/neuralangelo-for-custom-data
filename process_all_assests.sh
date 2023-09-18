#!/bin/bash

SCENE_TYPE="object"
GPUS=1
RESOLUTION=1024
BLOCK_RES=128

PARENT_DIRECTORY="custom_assets/assets"
IMAGE_FORMAT="heif"

for folder in "$PARENT_DIRECTORY"/*; do
        if [ -d "$folder" ]; then
            folder_name=$(basename "$folder")
            SEQUENCE=$folder_name
            GROUP="${SEQUENCE}_group"
            NAME=$SEQUENCE
            DATA_PATH="datasets/${folder_name}_ds2"
            OUTPUT_MESH="logs/${GROUP}/${NAME}/${SEQUENCE}_mesh.ply"
            CHECKPOINT="logs/${GROUP}/${NAME}/latest_checkpoint.pt" 
            TRAIN_CONFIG="projects/neuralangelo/configs/custom/${SEQUENCE}.yaml"
            MESH_CONFIG=logs/${GROUP}/${NAME}/config.yaml
            SOURCE_FOLDER="$folder"
            DESTINATION_FOLDER="datasets/${folder_name}_ds2/images_raw"

            if [ "$1" = "preparation" ]; then        
                echo "Performing preparation... $folder_name"

                python3 copy_input_images.py "$SOURCE_FOLDER" "$DESTINATION_FOLDER" "$IMAGE_FORMAT"
                bash projects/neuralangelo/scripts/run_colmap.sh "$DATA_PATH"
                python3 projects/neuralangelo/scripts/convert_data_to_json.py --data_dir "$DATA_PATH" --scene_type "$SCENE_TYPE"
                python3 projects/neuralangelo/scripts/generate_config.py --sequence_name "$SEQUENCE" --data_dir "$DATA_PATH" --scene_type "$SCENE_TYPE"

            elif [ "$1" = "training" ]; then
                echo "Performing training... $folder_name"

                torchrun --nproc_per_node=${GPUS} train.py --logdir=logs/${GROUP}/${NAME} --config=${TRAIN_CONFIG} --show_pbar --wandb --wandb_name="neuralangelo"
                
            elif [ "$1" = "extraction" ]; then
                echo "Extracting mesh... $folder_name"
                torchrun --nproc_per_node="$GPUS" projects/neuralangelo/scripts/extract_mesh.py --config="$MESH_CONFIG" --checkpoint="$CHECKPOINT" --output_file="$OUTPUT_MESH" --resolution="$RESOLUTION" --block_res="$BLOCK_RES" --textured
                
            else
                echo "Invalid argument. Please provide either 'preparation' or 'training'."
            fi
        fi
        # break
done

