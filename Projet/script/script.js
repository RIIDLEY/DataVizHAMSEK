$(document).ready(function () {
    $.ajax({
        url: 'data/images_data.csv',
        dataType: 'text',
    }).done(function (data) {
        var allRows = data.split(/\r?\n|\r/);
        var lien = document.getElementById('lien');

        for (var singleRow = 0; singleRow < 20; singleRow++) {
            var rowCells = allRows[singleRow].split(',');
            lien.innerHTML += '<section class="section__items"><a href="' + rowCells[2] + '" target="_blank"> <img src="' + rowCells[2] + '" alt="' + rowCells[2] + '" class="' + rowCells[2] + '"> </a></section>';
            console.log(rowCells);
        }
    });
});
