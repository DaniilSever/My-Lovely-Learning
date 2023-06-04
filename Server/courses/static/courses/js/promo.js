document.querySelector(".join-the-course-btn").addEventListener("click", () => {
    fetch($("#join-url").attr("data-url"), {
        method: "POST",
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
        }
    })
    .then(response => response.json())
	.then(data => {
        console.log(getCookie("csrftoken"));
        window.location = $("#first-lesson-url").attr("data-url")
    }
    )
	.catch(err => console.error(err));
})