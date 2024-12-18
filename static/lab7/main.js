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
    const film = {
        title: document.getElementById('title').value,
        title_ru: document.getElementById('title-ru').value,
        year: document.getElementById('year').value,
        description: document.getElementById('description').value
    }
    fetch('/lab7/rest-api/films', {
        method:'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(film)
    })
    .then(function() {
        fillFilmList();
        hideModal();
    })
}