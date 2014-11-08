/**
 * Simple app to post a name to the backend,
 *  then display a result returned.
 *
 * Author: Corwin Brown
 * Date: 11-7-14
 * E-Mail: blakfeld@gmail.com
 */

 $(document).ready(function () {
    $('#drawName').click(function(e) {
        e.preventDefault();
        $('#result').empty();
        $.ajax({
            url: '/drawName',
            method: 'POST',
            data: {
                'username': $('#username').val()
            },
            success: function (data) {
                console.log('Data ' + data);
                $('#result').append('<h2>' + data + '</h2>');
            }
        })
    })
 })
