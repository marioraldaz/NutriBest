import axios from "axios";

const UsersApi = axios.create({
  baseURL: "http://localhost:8000/api/",
});
export function getProfileByID(id) {
  // const res = axios.get());
}

export function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

export const setCookie = (name, value, options = {}) => {
  const { expires, path } = options;
  let cookieString = `${name}=${value}`;

  if (expires) {
    cookieString += `; expires=${expires.toUTCString()}`;
  }

  if (path) {
    cookieString += `; path=${path}`;
  }

  document.cookie = cookieString;
};

export const uploadProfilePicture = async (file) => {
  e.preventDefault();
  const formData = new FormData();
  formData.append("profile_picture", file);
  console.log(formData);
  try {
    const response = await axios.post(
      "http://localhost:8000/upload-profile-picture/",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );
    console.log("File uploaded:", response.data);
  } catch (error) {
    console.error("Error uploading file:", error);
  }
};
