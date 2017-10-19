var previous;

$(window).scroll(function () {
    if ($('.post').length) {
        var posicion = $(window).scrollTop();
        var posts = Math.floor($('.post:last').offset().top) - $(window).height();
        var next

        if (posicion >= posts) {
            if (!previous) {
                
                console.log("Es hora de recargar mas")
                postsListManager.loadposts(function (nextPage){
                    next = nextPage
                    console.log(next)
                });            
            } else if (previous == 1) {
                return false;
            }
        }
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

    loadposts: function (nextPage) {
        var self = this;
        // mostrar el mensaje de cargando
        self.setUiLoading();

        // cargamos los posts
        postservice.list(function (posts) { 
            if (posts.results.length == 0) {
                self.setUiBlank(); // si no hay posts -> estado en blanco
            } else {
                // pintar los posts en el listado
                nextPage(posts.next)
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
            html += '                            <a href="{% url "post-detail" blog_pk=post.blog.id post_pk=post.id %}">'+ post.title + '</a>'
            html += '                        </h2>'
            html += '                        <p>'+post.summary+'</p>'
            html += '                    </div>'
            html += '                    <div class="meta">'
            html += '                        <time class="publication-date">'+post.publication_date +'</time>'
            html += '                        <a href="#" class="author">'
            html += '                            <span class="name">'+post.blog.title+'</span>'
            html += '                            <img src='+ post.blog.logo? post.blog.logo : "https://www.hackster.io/assets/about/icon-blog-views-e31708c9be9be716040f0c09355b6a884fdbbdc2b171ccee3555cd89a2ad83da.png" +'class="border-tlr-radius">'
            html += '                        </a>'
            html += '                    </div>'
            html += '                </header>'
            html += '                <a href="#" class="image featured">'
            html += '                    <img src='+ post.image ? post.image : "http://lorempixel.com/400/200/sports/" +' alt=""'
            html += '                    />'
            html += '                </a>'
            html += '                <p>{% if post.content %} {{post.content}} {% else %} Mauris neque quam, fermentum ut nisl vitae, convallis maximus'
            html += '                    nisl. Sed mattis nunc id lorem euismod placerat. Vivamus porttitor magna enim, ac accumsan tortor cursus'
            html += '                    at. Phasellus sed ultricies mi non congue ullam corper. Praesent tincidunt sed tellus ut rutrum. Sed vitae'
            html += '                    justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla. {% endif %} </p>'
            html += '                <footer>'
            html += '                    <ul class="actions">'
            html += '                        <li>'
            html += '                            <a href="#" class="button big">Continue Reading</a>'
            html += '                        </li>'
            html += '                    </ul>'
            html += '                    <ul class="stats">'
            html += '                        <li>'
            html += '                            <a href="#"> {{ tag.name }} </a>'
            html += '                        </li>'
            html += '                        <li>'
            html += '                            <button class="btn btn-link">'
            html += '                                <i class="fa fa-bookmark" aria-hidden="true"> 7</i>'
            html += '                            </button>'
            html += '                            <button class="btn btn-link">'
            html += '                                <i class="fa fa-comments" aria-hidden="true"> 8</i>'
            html += '                            </button>'
            html += '                        </li>'
            html += '                    </ul>'
            html += '                </footer>'
            html += '            </article>'
            html += '        </div>'
            html += '    <div class="ui-error">'
            html += '        Se ha producido un error.'
            html += '    </div>'
            html += '    <div class="ui-blank">'
            html += '        <p>Aún no hay ningún posts.</p>'
            html += '    </div>'
            html += '    <div class="ui-loading">'
            html += '        Cargando...'
            html += '    </div>'
        }
        $(".comment:last").append(html);
    }
}


var postservice = {
    // recuperar todos los posts
    list: function (successCallback, errorCallback) {
        $.ajax({
            url: "http://127.0.0.1:8001/api/1.0/posts/",
            type: "get", // recuperar datos en una API REST
            success: function (data) {
                successCallback(data);
            },
            error: function (error) {
                errorCallback(error);
                console.error("postsServiceError", error);
            }
        });
    }
}





