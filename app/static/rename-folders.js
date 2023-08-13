const convertButton = document.getElementById("convert");
const directoryButton = document.getElementById("directory-button");
window.token = "{{ token }}";

directoryButton.addEventListener("click", async () => {
  $.get("/folders/directory", folderDirectory);
});

convertButton.addEventListener("click", () => {
  const directoryPath = document.getElementById("directory-input").value;
  const nameFormat = document.getElementById("name-format").value;
  const data = {
    directoryPath: directoryPath,
    nameFormat: nameFormat || "{id}",
  };
  data.token = window.token;
  console.log(data);
  $.ajax({
    type: "POST",
    url: "/folders/rename",
    data: JSON.stringify(data),
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    success: renameFolder,
  });
});

function folderDirectory(response) {
  if (response.status === "ok") {
    document.getElementById("directory-input").value = response.dir;
  }
}

function renameFolder(response) {
  console.log(response);
}
