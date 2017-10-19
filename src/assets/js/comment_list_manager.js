const $ = require('jquery');
const CommentService = require('./comment_service');
const date = require('./date');

module.exports = {

    loadComments: function(post_id){
        let self = this;             

        CommentService.list(post_id, function(comments){
            if (comments.length != 0){
                console.log(comments.results);
                self.renderComments(comments.results);
            }
        }, function(error){
            console.log(error);
        });
    },
    renderComments: function(comments){
        let html = '';
        for (let i in comments){
            let comment = comments[i];
            html+=' <div id="comments" class="card mb-3 card-comment">';
            html+= '    <div class="card-body">';
            html+='         <div class="meta">';
            html+='             <img src="'
            html+=  comment.owner.profile.avatar ?  comment.owner.profile.avatar :
                                    'https://www.hackster.io/assets/about/icon-blog-views-e31708c9be9be716040f0c09355b6a884fdbbdc2b171ccee3555cd89a2ad83da.png'  ;
            html+= '"'+'class="img-avatar">'
            html+='             <div class="author">';
            html+='                 <a>'+ comment.owner.username +'</a>';
            html+='                 <time class="publication-date">'+ date.dateFormat(comment.publication_date) + '</time>'
            html+='             </div>'
            html+=              parseInt(user)==comment.owner.id? '<a href="http://localhost:3000/'+ blog +"/"+ post+"/delete-comment/"+comment.id+ '" class="btn btn-danger button-delete" name="button-delete" > Borrar</a>': "" ;
            html+='         </div>'
            html+='         <div class="content">'
            html+=              comment.content
            html+='         </div>'
            html+='     </div>'
            html+='</div>'

           

        }
        $(".section-comments:last").append(html);
    }

}
