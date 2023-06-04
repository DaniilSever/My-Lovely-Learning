function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function myFetch (url="", _method="POST", _body=null) {
    fetch(url, {
        method: _method,
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            'Content-Type': 'application/json; charset=UTF-8',
        },
        body: _body
    })
    .then(response => response.json())
    .then(data => {return data})
    .catch(err => console.error(err))
}

function viewLessonContent (lesson, edit=false) {
    for (let content of lesson.lesson_contents) {
        let content_div = document.createElement('div')
        content_div.className = "lesson-content"
        let content_type = content.item.content_type
        if (content_type == "text") {
            content_div.className += " text"
            let text_content = document.createElement('p')
            text_content.innerHTML = content.item.content
            content_div.appendChild(text_content)
        } else if (content_type == "code") {
            content_div.className += " code"
            let pre_tag = document.createElement('pre')
            let code_tag = document.createElement('code')
            code_tag.className = `language-${content.item.language}`
            code_tag.innerHTML = content.item.content
            pre_tag.appendChild(code_tag)
            content_div.appendChild(pre_tag)
            hljs.highlightElement(code_tag)
        } else if (content_type == "image") {
            content_div.className += " image"
            let image_content = document.createElement('img')
            image_content.style = "width: 640px"
            image_content.src = content.item.file
            content_div.appendChild(image_content)
        } else if (content_type == "video") {
            content_div.className += " video"
            let video_content = document.createElement('iframe')
            video_content.className = "video-resourse"
            video_content.style = "width: 640px; height: 480px;"
            video_content.src = content.item.url
            video_content.setAttribute("allowfullscreen", "")
            content_div.appendChild(video_content)
        } else if (content_type == "writeaprogram") {
            content_div.className += " program"
            let program_form = document.createElement('form')
            program_form.setAttribute("method", "POST")
            let program_content = document.createElement('textarea')
            let program_launch = document.createElement('button')
            program_launch.innerHTML = "Запустить"
            program_launch.setAttribute("type", "submit")
            program_form.appendChild(program_content)
            program_form.appendChild(program_launch)
            program_form.addEventListener("submit", (ev) => {
                ev.preventDefault()
                fetch("/api/v1/compiler/", {
                    method: "POST",
                    credentials: "same-origin",
                    headers: {
                        "X-CSRFToken": getCookie("csrftoken"),
                        'Content-Type': 'application/json; charset=UTF-8',
                    },
                    body: JSON.stringify({
                        language: 'python',
                        user_input: program_content.value,
                    })
                })
                .then(response => response.json())
                .then(data => {})
                .catch(err => console.error(err))

                
            })
            if (edit) {
                program_content.disabled = true
                program_launch.disabled = true
            }
            content_div.appendChild(program_form)
        }
        document.querySelector('.lesson-contents').appendChild(content_div)
    }
}