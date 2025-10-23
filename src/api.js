// 🔗 Base API URL from environment
const BASE_URL = process.env.REACT_APP_API_URL || "https://siqnet.tech";

// 🧠 Helper: Handle API responses
async function handleResponse(response) {
  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: "Unknown error" }));
    throw new Error(error.detail || "Request failed");
  }
  return response.json();
}

// 📥 Fetch all posts
export async function fetchPosts() {
  try {
    const response = await fetch(`${BASE_URL}/siqposts/`, {
      credentials: "include",
    });
    return await handleResponse(response);
  } catch (error) {
    console.error("Error fetching posts:", error.message);
    return [];
  }
}

// 📝 Create a new post
export async function createPost(formData, token = null) {
  try {
    const response = await fetch(`${BASE_URL}/siqposts/create/`, {
      method: "POST",
      body: formData,
      credentials: "include",
      headers: token
        ? { Authorization: `Bearer ${token}` }
        : undefined,
    });
    return await handleResponse(response);
  } catch (error) {
    console.error("Error creating post:", error.message);
    return { error: error.message };
  }
}
