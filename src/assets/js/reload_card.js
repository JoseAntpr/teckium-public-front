const date = require('./date');
const likes = require('./likes');

$(window).scroll(function () {
    if($(window).scrollTop() + $(window).height() == $(document).height()) {
        postsListManager.loadposts();
    }
});

var postsListManager = {
    setUiIdeal: function () {
        $('.section-post').removeClass().addClass('section-post ideal');
    },

    setUiBlank: function () {
        $('.section-post').removeClass().addClass('section-post blank');
    },

    setUiError: function () {
        $('.section-post').removeClass().addClass('section-post error');
    },

    setUiLoading: function () {
        $('.section-post').removeClass().addClass('section-post loading');
    },

    loadposts: function () {
        var self = this;
        // mostrar el mensaje de cargando
        self.setUiLoading();

        // cargamos los posts
        postservice.list(function (posts) {
            if (posts.results.length == 0) {
                self.setUiBlank(); // si no hay posts -> estado en blanco
            } else {
                // pintar los posts en el listado
                self.renderposts(posts.results);
                self.setUiIdeal(); // ponemos el estado ideal
            }
        }, function (error) { // si se produce algún error
            self.setUiError(); // ponemos el estado error
        });
    },

    renderposts: function (posts) {
        var html = '';
        for (var i in posts) {
            var post = posts[i];
            html += '        <div class="col-md-12 col-12">'
            html += '            <article class="post">'
            html += '                <header>'
            html += '                    <div class="title">'
            html += '                        <h2>'
            html += '                            <a href="/'+post.blog.id+'/'+post.id +'">'+ post.title + '</a>'
            html += '                        </h2>'
            html += '                        <p>'+post.summary+'</p>'
            html += '                    </div>'
            html += '                    <div class="meta">'
            html += '                        <time class="publication-date">'+date.dateFormat(post.publication_date) +'</time>'
            html += '                        <a href="#" class="author">'
            html += '                            <span class="name">'+post.blog.title+'</span>'
            html +=                              post.blog.logo ? '<img src="'+post.blog.logo+'" class="border-tlr-radius">' : '<img src="https://www.hackster.io/assets/about/icon-blog-views-e31708c9be9be716040f0c09355b6a884fdbbdc2b171ccee3555cd89a2ad83da.png" class="border-tlr-radius">'
            html += '                        </a>'
            html += '                    </div>'
            html += '                </header>'
            html += '                <a href="#" class="image featured">'
            html +=                  post.image ? '<img src="'+ post.image +'" alt=""/>'  : '<img src="http://lorempixel.com/400/200/sports/" alt=""/>'
            html += '                </a>'
            html +=                  post.content ? '<p>'+ post.content +'</p>' : '<p>Mauris neque quam, fermentum ut nisl vitae, convallis maximus'
            html += '                    nisl. Sed mattis nunc id lorem euismod placerat. Vivamus porttitor magna enim, ac accumsan tortor cursus'
            html += '                    at. Phasellus sed ultricies mi non congue ullam corper. Praesent tincidunt sed tellus ut rutrum. Sed vitae'
            html += '                    justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla. </p>'
            html += '                <footer>'
            html += '                    <ul class="actions">'
            html += '                        <li>'
            html += '                            <a href="/'+post.blog.id+'/'+post.id +'" class="button big">Continue Reading</a>'
                                                 if(user == post.owner.id){
                                                    html += '<a href="/edit-post/' + post.id +'" class="btn btn-primary btn-xs"><span class="fa fa-pencil"></span></a>'
                                                    html += '<a href="/delete-post/' + post.id +'" class="btn btn-danger btn-xs"><span class="fa fa-trash"></span></a>'
                                                 }
            html += '                        </li>'
            html += '                    </ul>'
            html += '                    <ul class="stats">'
                                         post.tags.map(function(tag){
                                            html +='<li><a href="#">'+ tag.name +'</a></li>'
                                        })
            html += '                        <li>'
            html += '                            <button id="' + post.id + '" class="btn btn-link favourite-button" value="[' + post.likes + ']" data-action="'
                                                    if (user.id in post.likes){
                                                        html += 'unvote">'
                                                    }else {
                                                        html += 'upvote">'
                                                    } 
                                                    if (user.id in post.likes){
                                                        html += '<i class="fa fa-heart" aria-hidden="true">'+ post.likes.length +'</i>'
                                                    }else{
                                                        html += '<i class="fa fa-heart-o" aria-hidden="true">'+ post.likes.length +'</i>'
                                                    }
                                                    
                                                 html += '</button>'
            html += '                            <button class="btn btn-link">'
            html += '                                <i class="fa fa-comments" aria-hidden="true">'+ post.comments.length +'</i>'
            html += '                            </button>'
            html += '                        </li>'
            html += '                    </ul>'
            html += '                </footer>'
            html += '            </article>'
            html += '        </div>'
        }
        $(".section-post").append(html);
        $('.favourite-button').on("click", function(){
            likes.clickLike($(this));
        });
    }
}


var postservice = {
    // recuperar todos los posts
    list: function (successCallback, errorCallback) {
        if (typeof url !== 'undefined' && url && url != "None"){
            $.ajax({
                url: url,
                type: "get", // recuperar datos en una API REST
                success: function (data) {
                    console.log(url)
                        url = data.next;
                        successCallback(data);
                    
                },
                error: function (error) {
                    errorCallback(error);
                    console.error("postsServiceError", error);
                }
            });
        }
        
        postsListManager.setUiIdeal()
    }
}





