function deletePet(petId) {
  fetch("/delete-pet", {
    method: "POST",
    body: JSON.stringify({ petId: petId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}