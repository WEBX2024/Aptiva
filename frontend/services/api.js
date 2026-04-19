const BASE_URL = "http://localhost:8000";

export const uploadProfile = async (file, userId) => {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${BASE_URL}/profile/upload?user_id=${userId}`, {
    method: "POST",
    body: formData,
  });

  return res.json();
};

export const generateQueries = async (userId) => {
  const res = await fetch(`${BASE_URL}/query/generate?user_id=${userId}`);
  return res.json();
};

export const discoverJobs = async (query) => {
  const res = await fetch(`${BASE_URL}/jobs/discover?query=${query}`, {
    method: "POST",
  });
  return res.json();
};

export const scoreJobs = async (userId) => {
  const res = await fetch(`${BASE_URL}/score/jobs?user_id=${userId}`, {
    method: "POST",
  });
  return res.json();
};
