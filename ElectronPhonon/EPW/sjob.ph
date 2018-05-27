#!/bin/bash
#SBATCH --ntasks=32
#SBATCH --cpus-per-task=1
#SBATCH --job-name=ph
#SBATCH --mem-per-cpu=4000M
#SBATCH --time=96:00:00

#SBATCH --mail-user=ppdebreuck@hotmail.com
#SBATCH --mail-type=ALL
#SBATCH --partition=Def

module purge
source /home/ucl/naps/gbrunin/SetEnv.sh intel13_intel

export OMP_NUM_THREADS=1
unset SLURM_CPUS_PER_TASK

MPI="mpirun"
MPIOPT="-np 32"
QE="/home/ucl/naps/gbrunin/q-e/bin/ph.x"

${MPI} ${MPIOPT} ${QE} < ph.in > ph.out

echo "--"
