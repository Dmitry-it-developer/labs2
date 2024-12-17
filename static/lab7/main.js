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