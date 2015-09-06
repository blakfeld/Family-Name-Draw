<!DOCTYPE html>
<html>
<head>
    <title>Family Name Draw</title>

    <!-- JQuery -->
    <script src="//code.jquery.com/jquery-1.11.3.min.js"></script>

    <!--- Bootstrap -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

    <!-- FontAwesome -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">

    <!--- CSS -->
    <link rel="stylesheet" type="text/css" href="style.css">

    <!-- Javascript -->
    <script type="text/javascript" src="main.js"></script>

</head>
<body>
    <div id='errorModal' class="modal fade" role="dialog">
        <div class="modal-dialog">
            <div class="modal-header">
                <h2 class="modal-title text-center"><i class="fa fa-warning"></i>&nbsp;Error</h2>
            </div>
            <div id='errorModalBody' class='modal-body text-center'>
                <p>Invalid selection!</p>
            </div>
            <div class='model-footer text-center'>
                <button type='button' class='btn btn-danger center-block' data-dismiss='modal'>Close</button>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="page-header">
            <h1>Name Drawer</h1>
        </div>

        <div id="resultRow" class="row" style="display: none;">
            <div id="resultDisplay" class="col-md-12 text-center">
            </div>
        </div>
        <div id="selectRow" class="row">
            <div class="col-md-12">
                <form>
                    <div class="form-group">
                        <label for="name">Who are you?</label>
                        <select id="memberNames" disabled>
                            <option value="">Loading...</option>
                        </select>
                    </div>
                </form>
                <button id="drawName" type="submit" class="btn btn-primary pull-right" disabled>Draw Name</button>
            </div>
        </div>

    </div>
</body>
</html>
