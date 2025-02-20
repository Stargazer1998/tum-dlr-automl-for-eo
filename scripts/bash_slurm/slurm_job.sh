#!/bin/bash -x

#SBATCH --account=hai_nasb_eo
#SBATCH --partition=develbooster # booster or develbooster number of gpus per node
#SBATCH --gres=gpu:4   
#SBATCH --job-name=torch-test   
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)   
#SBATCH --time=01:00:00          # total run time limit (HH:MM:SS)
#SBATCH --output=gpu-out.%j
#SBATCH --error=gpu-err.%j

# go to the repository directory                                                                                                                                                                                   
cd /p/project/hai_nasb_eo/emre/tum-dlr-automl-for-eo/

# connect interactively to the compute node for experiments
srun /p/project/hai_nasb_eo/emre/tum-dlr-automl-for-eo/scripts/bash_slurm/script_experiments.sh ${1}