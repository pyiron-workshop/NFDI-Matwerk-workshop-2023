for i in range(2, 9):
    job=pr.create_job(job_type=YoungsModulusJob, job_name=f'y{i}', delete_existing_job=True)
    job.input.filename = f'tensile_test/dataset_{i}.csv'
    job.input.area = 120.636
    job.run()