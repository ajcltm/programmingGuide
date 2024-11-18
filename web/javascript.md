
### load fragment
~~~javascript
document.addEventListener('DOMContentLoaded', webinfolist);  
async function webinfolist() {  
    await loadFragment("/webinfo/webinfolist", "webinfolist");  
    await registerModal()  
    document.getElementById('webinfolist').addEventListener('click', (e) => {  
        if (e.target.classList.contains('item-modify-btn')) {  
            modify(e);  
        } else if (e.target.classList.contains('item-done-btn')) {  
            submitForm(e);  
        } else if (e.target.classList.contains('item-remove-btn')) {  
            remove(e);  
        } else if (e.target.classList.contains('item-cancel-btn')) {  
            loadFragment("/webinfo/webinfolist", "webinfolist");  
        } else if (e.target.classList.contains('register-submit')) {  
            registerSubmit(e);  
        }  
    });  
}  
  
async function loadFragment(url, elementId) {  
    await fetch(url)  
        .then(response => {  
            if (!response.ok) {  
                throw new Error('Network response was not ok');  
            }  
            return response.text();  
        })  
        .then(data => {  
            document.getElementById(elementId).innerHTML = data;  
        })  
        .catch(error => {  
            console.error('There was a problem with the fetch operation:', error);  
        });  
}
~~~

#### form data
~~~javascript
async function submitForm(event) {  
    event.preventDefault();
    const form = document.getElementById('modify-form');
    const formData = new FormData(form);  
	await fetchPost(formData);  
}  
  
function fetchPost(formData) {  
    fetch('/webinfo/modify', {  
        method: 'POST',  
        body:formData  
    })  
        .then(response => {  
            if (response.ok) {  
                return response.text()  
            }  
        })  
        .then(data => {  
            document.getElementById("webinfolist").innerHTML = data;  
        });  
}
~~~