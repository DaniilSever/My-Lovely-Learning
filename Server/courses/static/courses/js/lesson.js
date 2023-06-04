let my_data
const SPAN_STYLE = "display: inline-block; width: 30px; height: 30px; border: 1px solid; border-radius: 5px; margin-right: 3px;"

function clearSelectedLesson (parent) {
    for (const child of parent.children) {
        if (child.className == "add-lesson-button") return
        child.style = "background-color: grey; display: inline-block; width: 30px; height: 30px; border: 1px solid; border-radius: 5px; margin-right: 3px"
    }
}

function createElementForLessonStudent (lesson) {
    let lesson_btn = document.createElement("span")

    lesson_btn.style = SPAN_STYLE + "background-color: grey;"
    lesson_btn.addEventListener('click', (event) => {
        clearSelectedLesson(event.target.parentNode)
        document.querySelector(".lesson-contents").innerHTML = ""
        event.target.style = SPAN_STYLE + "background-color: green;"

        let lesson_theme_div = document.createElement("div")
        lesson_theme_div.className = "lesson-theme"
        
        let lesson_theme = document.createElement("h4")
        lesson_theme.className = "theme"
        lesson_theme.innerHTML = lesson.theme

        lesson_theme_div.appendChild(lesson_theme)
        document.querySelector(".lesson-contents").appendChild(lesson_theme_div)

        console.log(lesson)
        
        viewLessonContent(lesson)


    })
    document.querySelector(".lesson-switcher").appendChild(lesson_btn)
}


$(document).ready(() => {
    fetch($("#api-get-subchapter-content").attr("data-url"), {
        method: "GET",
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            'Content-Type': 'application/json; charset=UTF-8',
        }
    })
    .then(response => response.json())
    .then(data => {

        for (const lesson of data.lessons) {
            createElementForLessonStudent(lesson)
        }
        my_data = data
    })
    .catch(err => console.error(err))
})