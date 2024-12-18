function fillFilmList() {
    fetch('/lab7/rest-api/films', {method: 'GET'})
    .then(function(data) {
        return data.json()
    })
    .then(function(films) {
        let tbody = document.getElementById('film-list');
        tbody.innerHTML = '';
        for (let i = 0; i < films.length; i++) {
        
            let tr = document.createElement('tr');

            let tdTitle = document.createElement('td');
            tdTitle.innerText = films[i].title == films[i].title_ru ? '': films[i].title;
            let tdTitleRus = document.createElement('td');
            tdTitleRus.innerText = films[i].title_ru;
            let tdYear = document.createElement('td');
            tdYear.innerText = films[i].year;
            let tdActions = document.createElement('td');
            
            let editButton = document.createElement('button');
            editButton.innerText = 'Редактировать';
            editButton.onclick = function () {
                editFilm(i);
            }

            let deleteButton = document.createElement('button');
            deleteButton.innerText = 'Удалить';
            deleteButton.onclick = function() {
                deleteFilm(i, films[i].title_ru);
            }
            tdActions.append(editButton, deleteButton);

            tr.append(tdTitle, tdTitleRus, tdYear, tdActions);

            tbody.append(tr);
        }
    })
}

function deleteFilm(id, title_ru) {
    if (!confirm(`Вы точно хотите удалить фильм ${title_ru}?`))
        return;
    fetch(`/lab7/rest-api/films/${id}`, {method: 'DELETE'})
    .then(function() {
        fillFilmList();
    });
}

function showModal() {
    document.querySelector('div.modal').style.display = 'block';
}

function hideModal() {
    document.querySelector('div.modal').style.display = 'none';
}

function addFilm() {
    document.getElementById('id').value = '';
    document.getElementById('title').value = '';
    document.getElementById('title-ru').value = '';
    document.getElementById('year').value = '';
    document.getElementById('description').value = '';
    showModal()
}

function cancel() {
    hideModal()
}

function sendFilm() {
    const id = document.getElementById('id').value;
    const film = {
        title: document.getElementById('title').value,
        title_ru: document.getElementById('title-ru').value,
        year: document.getElementById('year').value,
        description: document.getElementById('description').value
    }
    const url = `/lab7/rest-api/films/${id}`
    const method = id == '' ? 'POST' : 'PUT'
    fetch(url, {
        method: method,
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(film)
    })
    .then(function() {
        fillFilmList();
        hideModal();
    })
}

function editFilm(id) {
    fetch(`/lab7/rest-api/films/${id}`)
    .then(function(data) {
        return data.json();
    })
    .then(function(film) {
        console.log(film);
        document.getElementById('id').value = id;
        document.getElementById('title').value = film.title;
        document.getElementById('title-ru').value = film.title_ru;
        document.getElementById('year').value = film.year;
        document.getElementById('description').value = film.description;
        showModal();
    })

}

