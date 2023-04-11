function displayPost(post){
    var container = document.querySelector('ol');
    
    var html = 
    `<li class="timeline-item">
        <div class="post-container">
            <div class="poster1">
                <a class="profilelink" href="#">
                    <img class="profilePic" src="graphics/profile_pics/IMG-9004.jpg" alt="">
                    <span class="profiletxt-board">@${post.author}</span>
                </a>
            </div>
        
            <div class="content">
                <p class="content-txt">
                    ${post.content}
                </p>
            </div>
            <div class="bottom">
                <p class="timestamp">
                    <span class="time">${post.date}</span>
                    <span class="date">${post.time}</span>
                </p>
                <div class="reaction-btns">
                    <span class="like-count"> ${post.like_count} </span>
                    <input class="like-btn" type="image" src="graphics/icons/icons8-heart-52.png">
                    <span class="comment-count"> ${post.comment_count} </span>
                    <input class="comment-btn" type="image" src="graphics/icons/icons8-comments-52.png">
                    <span class="repost-count"> ${post.repost_count} </span>
                    <input class="repost-btn" type="image" src="graphics/icons/icons8-retweet-48.png">
                </div>
            </div>
        </div>
    </li>
    `
    container.insertAdjacentHTML('afterbegin', html);
}

function Post(author, date, time, content, like_count, comment_count, repost_count, comments){
    this.author = author;
    this.date = date;
    this.time = time;
    this.content = content;
    this.like_count = like_count.toString();
    this.comment_count = comment_count.toString();
    this.repost_count = repost_count.toString();
    this.comments = comments;
}

function addZero(num){
    return num < 10 ? `0${num}`:num;
}

function currentDate() {
    let today = new Date();

    let month = today.getMonth()+1;
    let year = today.getFullYear();
    let date = today.getDate();
    return `${month}/${date}/${year}`;
}

function currentTime(){
    let today = new Date();

    let hours = addZero(today.getHours());
    let minutes = addZero(today.getMinutes());

    if (hours > 12) {
        hours = hours-12;
        let current_time = `${hours}:${minutes} PM`;
        return current_time;
    }
    else {
        let current_time = `${hours}:${minutes} AM`;
        return current_time;
    }
}
var post1 = new Post("kennywang", currentDate(), currentTime(), "This is my tweet!", 0, 0, 0);

var threads = [post1];