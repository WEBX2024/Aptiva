import UploadForm from "../components/UploadForm";
import JobList from "../components/JobList";
import { useJobs } from "../hooks/useJobs";

function App() {
  const { jobs, runPipeline } = useJobs();

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">AI Job Agent</h1>

      <UploadForm onUpload={runPipeline} />

      <button
        className="mt-4 px-4 py-2 bg-green-600 text-white"
        onClick={runPipeline}
      >
        Run Job Pipeline
      </button>

      <JobList jobs={jobs} />
    </div>
  );
}

export default App;
