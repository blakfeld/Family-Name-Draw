/*
 * Main Controller logic for this dinky Name Draw App
 */

var availablemembers;

function showErrorMsg() {
    $('#errorModal').modal('show');
}

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function getMemberData() {
    $.ajax({
        url: '/api/members',
        method: 'GET',
        success: function(data) {
            populateDropdown(data.members);

            $('#memberNames').prop('disabled', false);

            return data.members;
        }
    });
}

function checkValidMember(currentUser) {
    $.ajax({
        url: '/api/members/' + currentUser,
        method: 'GET',
        success: function(data) {
            member = data.members[0]
            if (member.has_chosen != 0) {
                showAlreadyChosen();
            } else {
                getAvailableMembers(currentUser);
            }

        }
    })
}

function getAvailableMembers(currentUser) {
    $.ajax({
        url: '/api/availablemembers/' + currentUser,
        method: 'GET',
        success: function(data) {
            members = data.members;
            availablemembers = members;

            $('#drawName').prop('disabled', false);
        }
    });
}

function submitChosenName(currentUser, chosenUser) {
    jsonBody = {
        'chosenUserId': chosenUser.id
    }

    $.ajax({
        url: '/api/members/' + currentUser,
        method: 'PUT',
        contentType: 'application/json',
        data: JSON.stringify(jsonBody),
        dataType: 'json',
        success: function() {
            console.log('yes?');
        }
    });
}

function populateDropdown(members) {
    if (!members || members === '') {
        console.log('Something died?');
    }

    $('#memberNames').empty();

    defaultOption = '<option value="-1">Select your name...</option>'
    $('#memberNames').append(defaultOption);

    members.forEach(function (member) {
        memberSelectOption = '<option value="' + member.id + '">' + member.name + '</option>';
        $('#memberNames').append(memberSelectOption);
    })
}

function showAlreadyChosen() {
    $('#resultDisplay').empty()
    $('#resultDisplay').append("<h2>You've already chosen!</h2>")

    $('#resultRow').slideDown();
    $('#selectRow').fadeOut();
}

function showResult(result) {
    $('#resultDisplay').empty()
    $('#resultDisplay').append('You got: <h1>' + result.name + '</h2>')

    $('#resultRow').slideDown();
    $('#selectRow').fadeOut();
}

$(document).ready(function() {
    var members = getMemberData();

    $('#memberNames').change(function(e) {
        if ($('#memberNames').val() === "-1") {
            showErrorMsg();
        } else {
            checkValidMember($('#memberNames').val());
        }
    });

    $('#drawName').click(function(e) {
        e.preventDefault();

        index = getRandomNumber(0, availablemembers.length - 1);
        chosenUser = availablemembers[index];
        console.log('Available: ' + availablemembers + '\nLength: ' + availablemembers.length + '\nIndex: ' + index + '\nChosen: ' + chosenUser);
        submitChosenName($('#memberNames').val(), chosenUser);
        showResult(chosenUser);
    });
})
