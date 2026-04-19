import { useState } from "react";
import { uploadProfile } from "../services/api";

function UploadForm({ onUpload }) {
  const [file, setFile] = useState(null);

  const handleSubmit = async () => {
    if (!file) return;

    const res = await uploadProfile(file, 1);
    onUpload(res);
  };

  return (
    <div className="p-4 border rounded">
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button
        className="mt-2 px-4 py-2 bg-blue-500 text-white"
        onClick={handleSubmit}
      >
        Upload Resume
      </button>
    </div>
  );
}

export default UploadForm;
