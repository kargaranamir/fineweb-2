from datatrove.executor import SlurmPipelineExecutor
from datatrove.pipeline.readers import ParquetReader
from datatrove.pipeline.writers import JsonlWriter

SlurmPipelineExecutor(
    pipeline=[
        ParquetReader("hf://datasets/vngrs-ai/vngrs-web-corpus", glob_pattern="data/*.parquet", id_key="original_id", default_metadata={"language": "tr"}),
        JsonlWriter("/path/to/ref-datasets/monolingual/tr/vngrs",
                    output_filename="${rank}.jsonl.gz", max_file_size=2*2**30)
    ],
    tasks=64,
    randomize_start_duration=3 * 60,
    time="11:59:59",
    job_name="dl_vngrs",
    cpus_per_task=64,
    mem_per_cpu_gb=1,
    partition="partition",
    srun_args={"environment": "train"},
    logging_dir="/path/to/logs/dataset_download_logs/tr/vngrs",
).run()