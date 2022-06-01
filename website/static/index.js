function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function deletePet(petId) {
  fetch("/delete-pet", {
    method: "POST",
    body: JSON.stringify({ petId: petId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

