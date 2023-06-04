const SPAN_STYLE = "display: inline-block; width: 30px; height: 30px; border: 1px solid; border-radius: 5px; margin-right: 3px;"
const api_subchapter_contents_link = $("#api-subchapter-link").attr("data-url")
const api_add_lesson_link = $("#api-add-lesson-link").attr("data-url")
const svg_gear = '<svg fill="#000000" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 45.973 45.973" xml:space="preserve"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g> <g> <path d="M43.454,18.443h-2.437c-0.453-1.766-1.16-3.42-2.082-4.933l1.752-1.756c0.473-0.473,0.733-1.104,0.733-1.774 c0-0.669-0.262-1.301-0.733-1.773l-2.92-2.917c-0.947-0.948-2.602-0.947-3.545-0.001l-1.826,1.815 C30.9,6.232,29.296,5.56,27.529,5.128V2.52c0-1.383-1.105-2.52-2.488-2.52h-4.128c-1.383,0-2.471,1.137-2.471,2.52v2.607 c-1.766,0.431-3.38,1.104-4.878,1.977l-1.825-1.815c-0.946-0.948-2.602-0.947-3.551-0.001L5.27,8.205 C4.802,8.672,4.535,9.318,4.535,9.978c0,0.669,0.259,1.299,0.733,1.772l1.752,1.76c-0.921,1.513-1.629,3.167-2.081,4.933H2.501 C1.117,18.443,0,19.555,0,20.935v4.125c0,1.384,1.117,2.471,2.501,2.471h2.438c0.452,1.766,1.159,3.43,2.079,4.943l-1.752,1.763 c-0.474,0.473-0.734,1.106-0.734,1.776s0.261,1.303,0.734,1.776l2.92,2.919c0.474,0.473,1.103,0.733,1.772,0.733 s1.299-0.261,1.773-0.733l1.833-1.816c1.498,0.873,3.112,1.545,4.878,1.978v2.604c0,1.383,1.088,2.498,2.471,2.498h4.128 c1.383,0,2.488-1.115,2.488-2.498v-2.605c1.767-0.432,3.371-1.104,4.869-1.977l1.817,1.812c0.474,0.475,1.104,0.735,1.775,0.735 c0.67,0,1.301-0.261,1.774-0.733l2.92-2.917c0.473-0.472,0.732-1.103,0.734-1.772c0-0.67-0.262-1.299-0.734-1.773l-1.75-1.77 c0.92-1.514,1.627-3.179,2.08-4.943h2.438c1.383,0,2.52-1.087,2.52-2.471v-4.125C45.973,19.555,44.837,18.443,43.454,18.443z M22.976,30.85c-4.378,0-7.928-3.517-7.928-7.852c0-4.338,3.55-7.85,7.928-7.85c4.379,0,7.931,3.512,7.931,7.85 C30.906,27.334,27.355,30.85,22.976,30.85z"></path> </g> </g> </g></svg>'
const edit_lesson_api_link = "/api/v1/course/lesson"
let my_data


function parseLesson (lesson) {
    let result = {
        "id": lesson.id,
        "theme": lesson.theme,
        "lesson_contents": lesson.lesson_contents
    }
    return result
}

function clearSelectedLesson (parent) {
    for (const child of parent.children) {
        if (child.className == "add-lesson-button") return
        child.style = "background-color: grey; display: inline-block; width: 30px; height: 30px; border: 1px solid; border-radius: 5px; margin-right: 3px"
    }
}

function addEventListenerOnAddContentLessonBtn (type=null, lesson=null) {
    let new_content_entry = document.querySelector(".add-lesson-btns").parentNode
    new_content_entry.innerHTML = ''
    switch (type) {
        case "text":
            let my_new_text_content = document.createElement('textarea')
            my_new_text_content.className = "my-text-content"

            my_new_text_content.addEventListener('focusout', (e) => {
                let text_value = e.target.value
                my_text_body = JSON.stringify({
                    content: text_value
                })
                myFetch(`/api/v1/course/add_lesson_content/${lesson.id}/${type}/`, _method="POST", _body=my_text_body)
                window.location.reload()
            })
            new_content_entry.appendChild(my_new_text_content); break;
        case "code":
            let my_new_code_content = document.createElement('form')
            my_new_code_content.setAttribute('method', "POST")
            my_new_code_content.class = 'my-code-content'

            my_new_code_content.innerHTML = `<select name="language-list" class="language-list" id="language-list">
                <option value="python">Python</option>
                <option value="c">C</option>
                <option value="cs">C#</option>
                <option value="cpp">C++</option>
            </select>
            <textarea class="textarea-add-code"></textarea>
            <button type="submit">Добавить</button>`
            my_new_code_content.addEventListener("submit", (e) => {
                e.preventDefault()
                my_code_body = JSON.stringify({
                    content: document.querySelector(".textarea-add-code").value,
                    language: document.querySelector(".language-list").value
                })
                myFetch(`/api/v1/course/add_lesson_content/${lesson.id}/${type}/`, _method="POST", _body=my_code_body)
                window.location.reload()
            })
            new_content_entry.appendChild(my_new_code_content); break;
        case "image":
            let my_new_image_content = document.createElement('form')
            my_new_image_content.setAttribute('method', "POST")
            my_new_image_content.class = 'my-image-content'

            my_new_image_content.innerHTML = `<input type="file" id="myFile" class="myFile" name="filename">
            <button type="submit">Добавить</button>`
            my_new_image_content.addEventListener("submit", (e) => {
                e.preventDefault()
                let form_data = new FormData()
                form_data.append('file', document.querySelector(".myFile").files[0])
                // myFetch(, _method="POST", _body=my_image_body)
                // 
                fetch(`/api/v1/course/add_lesson_content/${lesson.id}/${type}/`, {
                    method: "POST",
                    headers: {
                        "X-CSRFToken": getCookie("csrftoken")
                    },
                    body: form_data
                })
                .then(response => response.json())
                .then(data => {
                    window.location.reload()
                })
                .catch(err => console.error(err))
            })
            new_content_entry.appendChild(my_new_image_content); break;
        case "video":
            let my_new_video_content = document.createElement('input')
            my_new_video_content.className = "my-text-content"

            my_new_video_content.addEventListener('focusout', (e) => {
                let text_value = e.target.value
                my_text_body = JSON.stringify({
                    url: text_value
                })
                myFetch(`/api/v1/course/add_lesson_content/${lesson.id}/${type}/`, _method="POST", _body=my_text_body)
                window.location.reload()
            })
            new_content_entry.appendChild(my_new_video_content); break;
        case "writeaprogram":
            myFetch(`/api/v1/course/add_lesson_content/${lesson.id}/${type}/`, _method="POST")
            window.location.reload(); break;
    }
    
}

function addLessonContent (lesson) {
    let add_lesson_content_button = document.createElement("button")
    add_lesson_content_button.innerHTML = 'Добавить'
    add_lesson_content_button.style = "width: 50%; height: 100px; opacity: 0.4; border: dashed 2px grey; border-radius: 5px;"
    add_lesson_content_button.addEventListener('click', (eve) => {

        let lesson_content_select_buttons = document.createElement('div')
        let ul_content_select_buttons = document.createElement('ul')
        ul_content_select_buttons.className = "add-lesson-btns"

        ul_content_select_buttons.innerHTML = `<li><span class="add-lesson-content-btn text-btn"></span></li><li><span class="add-lesson-content-btn code-btn"></span></li><li>
        <span class="add-lesson-content-btn image-btn"></span></li><li><span class="add-lesson-content-btn video-btn"></span></li><li><span class="add-lesson-content-btn program-btn"></span></li>`

        lesson_content_select_buttons.appendChild(ul_content_select_buttons)
        
        eve.target.replaceWith(lesson_content_select_buttons)

        document.querySelectorAll(".add-lesson-btns > li > span").forEach(btn => {
            btn.addEventListener('click', (event) => {
                let klass_name = event.target.className
                switch (klass_name) {
                    case "add-lesson-content-btn text-btn": addEventListenerOnAddContentLessonBtn("text", lesson=lesson); break;
                    case "add-lesson-content-btn code-btn": addEventListenerOnAddContentLessonBtn("code", lesson=lesson); break;
                    case "add-lesson-content-btn image-btn": addEventListenerOnAddContentLessonBtn("image", lesson=lesson); break;
                    case "add-lesson-content-btn video-btn": addEventListenerOnAddContentLessonBtn("video", lesson=lesson); break;
                    case "add-lesson-content-btn program-btn": addEventListenerOnAddContentLessonBtn("writeaprogram", lesson=lesson); break;
                }
            })
        })
    })


    document.querySelector('.lesson-contents').appendChild(add_lesson_content_button)
}

function createElementForLesson (add=false, lesson=null) {
    let lesson_btn = document.createElement("span")
    if (add) {
        lesson_btn.className = "add-lesson-button"
        lesson_btn.style = SPAN_STYLE + "background: rgba(128, 128, 128, 0.3);"
        lesson_btn.addEventListener('click', (event) => {
            clearSelectedLesson(event.target.parentNode)
            document.querySelector(".lesson-contents").innerHTML = ""
            event.target.style = SPAN_STYLE + "background: rgba(128, 128, 128, 0.3);"
            
            myFetch(url=api_add_lesson_link, _method="POST")
            
            window.location.reload()
        })
    } else {
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

            let edit_theme_btn = document.createElement("span")
            edit_theme_btn.className = "edit-lesson-theme-btn"
            edit_theme_btn.style = "display: inline-block; width: 20px; height: 20px; opacity: 0.4;"
            edit_theme_btn.innerHTML = svg_gear
            edit_theme_btn.addEventListener('click', (event) => {
                let theme_input = document.createElement("input")
                theme_input.className = "lesson-theme-input"
                theme_input.value = lesson.theme
                theme_input.addEventListener("focusout", (e) => {
                    let inp_value = e.target.value
                    theme_input.replaceWith(lesson_theme)
                    lesson_theme.innerHTML = inp_value
                    myFetch(`${edit_lesson_api_link}/${lesson.id}/`, _method="PATCH", _body=JSON.stringify({theme: inp_value}))
                })

                lesson_theme.replaceWith(theme_input)
                
            })
            lesson_theme_div.appendChild(edit_theme_btn)
            lesson_theme_div.appendChild(lesson_theme)
            document.querySelector(".lesson-contents").appendChild(lesson_theme_div)

            viewLessonContent(lesson, edit=true)
            addLessonContent(lesson)


        })
    }
    document.querySelector(".lesson-switcher").appendChild(lesson_btn)
}


$(document).ready(() => {
    fetch(api_subchapter_contents_link, {
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
            let l = parseLesson(lesson)
            createElementForLesson(add=false, lesson)
        }
        createElementForLesson(add=true)
        my_data = data
    })
    .catch(err => console.error(err))
})