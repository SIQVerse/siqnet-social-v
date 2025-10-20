const BASE_URL = "https://your-backend-domain.com"; // Replace with actual backend URL

export async function fetchPosts() {
  const response = await fetch(`${BASE_URL}/siqposts/`, {
    credentials: "include",
  });
  return await response.json();
}

export async function createPost(formData) {
  const response = await fetch(`${BASE_URL}/siqposts/create/`, {
    method: "POST",
    body: formData,
    credentials: "include",
  });
  return await response.json();
}
