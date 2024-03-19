function convertImageToBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => {
      const base64String = reader.result.split(",")[1]; // Extract the Base64 part
      resolve(base64String);
    };
    reader.onerror = (error) => {
      reject(error);
    };
  });
}

export default convertImageToBase64;
