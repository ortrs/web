$(document).ready(function(){
    $.getJSON("art_database_archive.json", function(data){
        var tmp = '';
        tmp += '<div class="container-fluid">\n';
        tmp += '<div class="row">\n';
        $.each( data.artwork.pieces, function( key, props ) {
            console.log("Trying to unpack the json");
            console.log(props.img);

            tmp += '<div class="col-md-4 col-sm-6">\n';
            tmp += '    <div class="item">\n';
            tmp += '        <div class="thumb">\n';
            tmp += '            <a href="'+props.img+'" data-lightbox="image-1">\n';
            tmp += '            <div class="hover-effect">\n';
            tmp += '             <div class="hover-content">\n';            
            tmp += '             <h2>' + props.title + '</h2>\n';
            tmp += '             <p>' + props.size + '</p>\n';
            tmp += '             </div></div></a>\n';
            tmp += '             <div class="image">\n'; 
            tmp += '             <img src="' + props.thumb + '" loading="lazy">\n';
            tmp += '              </div>\n';
            tmp += '         </div>\n';        
            tmp += '      </div>\n';
            tmp += '  </div>\n';
            });
        tmp += '  </div>\n'
        tmp += '  </div>\n'
        tmp += '  <h2>Movement</h2>\n'
        tmp += '  <p>Here some evolution of artwork.</p>\n'
        $('.fourth-content').append(tmp);
    }).fail(function(){
        console.log("An error has occurred.");
    });
});