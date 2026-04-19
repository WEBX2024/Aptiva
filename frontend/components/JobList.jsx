function JobList({ jobs }) {
  return (
    <div className="mt-4">
      <h2 className="text-xl font-semibold">Job Results</h2>
      <ul className="mt-2 space-y-2">
        {jobs.map((job) => (
          <li key={job.job_id} className="p-3 border rounded">
            <div className="font-bold">{job.title}</div>
            <div className="text-sm text-gray-600">Score: {job.score}</div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default JobList;
