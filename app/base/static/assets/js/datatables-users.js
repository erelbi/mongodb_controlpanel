$(document).ready(function() {
    $('#usertable').DataTable( {
        dom: 'Bfrtip',
        buttons: [
            {
                text: 'Create',
                action: function ( e, dt, node, config ) {
                    document.getElementById('createbutton').click()
                }
            }
        ]
    } );
} );
