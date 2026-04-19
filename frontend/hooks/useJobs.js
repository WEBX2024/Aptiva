import { useState } from "react";
import { generateQueries, discoverJobs, scoreJobs } from "../services/api";

export const useJobs = () => {
  const [jobs, setJobs] = useState([]);

  const runPipeline = async () => {
    // Step 1: Generate queries
    const queryRes = await generateQueries(1);

    // simple extraction (basic)
    const queryText = queryRes.queries.split("\n")[1] || "Developer";

    // Step 2: Discover jobs
    await discoverJobs(queryText);

    // Step 3: Score jobs
    const scored = await scoreJobs(1);

    setJobs(scored);
  };

  return { jobs, runPipeline };
};
