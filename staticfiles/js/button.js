document.addEventListener('DOMContentLoaded', function () {

    function detailSeleksi() {
        var splide1 = new Splide('#detail-carousel');
        splide1.mount();
        let semuaBtn = document.querySelectorAll("#btn-menu button")
        semuaBtn[0].classList.add("text-[#FF6A88]", "font-bold")
        semuaBtn.forEach((e, i) => {

            e.addEventListener("click", (el) => {
                semuaBtn.forEach(elm => elm.classList.remove("text-[#FF6A88]", "font-bold"))
                splide1.go(i)
                e.classList.add("text-[#FF6A88]", "font-bold");
            });

        })
    }

    



    function detailGambar() {
        var splide2 = new Splide('#main-carousel', {
            pagination: false,
            drag: false,
            rewind: true,
        });

        var thumbnails = document.getElementsByClassName('thumbnail');
        var current;

        for (var i = 0; i < thumbnails.length; i++) {
            initThumbnail(thumbnails[i], i);
        }

        function initThumbnail(thumbnail, index) {
            thumbnail.addEventListener('click', function () {
                splide2.go(index);
            });
        }

        splide2.on('mounted move', function () {
            var thumbnail = thumbnails[splide2.index];

            if (thumbnail) {
                if (current) {
                    current.classList.remove("is-active2",);
                }

                thumbnail.classList.add("is-active2",);
                current = thumbnail;
            }
        });

        splide2.mount();
    }

    detailGambar()
    detailSeleksi()
});