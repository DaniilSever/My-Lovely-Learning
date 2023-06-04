let add_chapter_btn = document.querySelector(".add-chapter-btn")
let add_subchapter_btns = document.querySelectorAll(".add-subchapter-btn")

add_chapter_btn.onclick = function(event) {
    let syllabus = event.target.parentNode.parentNode
    let inp = document.createElement("input")
    inp.className = "chapter-input-title"
    inp.addEventListener('focusout', (e) => {
        let inp_val = e.target.value
        let li_chapter = document.createElement("li")
        li_chapter.className = "subchapter"
        li_chapter.style = "margin-left: 5px;"
        let label_chapter = document.createElement("h4")
        label_chapter.className = ""
        label_chapter.innerHTML = inp_val

        fetch($("#add-chapter-url").attr("data-url"), {
            method: "POST",
            credentials: "same-origin",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
                'Content-Type': 'application/json; charset=UTF-8',
            },
            body: JSON.stringify({
                title: inp_val
            })
        })
        .then(response => response.json())
        .then(data => {
            window.location.reload()
        })
        .catch(err => console.error(err));

        li_chapter.innerHTML = label_chapter.outerHTML
        e.target.replaceWith(li_chapter)
    })
    // let c_b = event.target.insertAdjacentHTML("beforebegin", inp.outerHTML);
    syllabus.insertBefore(inp, event.target.parentNode)
}

function addEvListenersOnSubchapters() {
    add_subchapter_btns.forEach(add_subchapter_btn => {
        add_subchapter_btn.onclick = function(event) {
            let chapter = event.target.parentNode.parentNode
            let inp = document.createElement("input")
            inp.className = "subchapter-input-title"
            inp.addEventListener('focusout', (e) => {
                let inp_value = e.target.value
                let li_subchapter = document.createElement("li")
                li_subchapter.className = "subchapter"
                li_subchapter.style = "margin-left: 17px;"
                let label_subchapter = document.createElement("h6")
                label_subchapter.className = ""
                label_subchapter.innerHTML = inp_value

                let chapter_id = event.target.parentNode.parentNode.parentNode.getAttribute("chapter-id")

                fetch(`/api/v1/course/add_subchapter/${chapter_id}/`, {
                    method: "POST",
                    credentials: "same-origin",
                    headers: {
                        "X-CSRFToken": getCookie("csrftoken"),
                        'Content-Type': 'application/json; charset=UTF-8',
                    },
                    body: JSON.stringify({
                        title: inp_value
                    })
                })
                .then(response => response.json())
                .then(data => {
                    window.location.reload()
                })
                .catch(err => console.error(err))

                li_subchapter.innerHTML = label_subchapter.outerHTML
                e.target.replaceWith(li_subchapter)
            })
            chapter.insertBefore(inp, event.target.parentNode)
        }
    })
}

addEvListenersOnSubchapters()