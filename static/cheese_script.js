init_app()

function init_app(){
    
  
    $(document).ready(function () {
        $('.more-cheese-info').click(function (event) {
            /* DATA FROM */
            var $row = $(this).parents('tr');
            var row_num = $row.find('input[name="rownum"]').val();
            var province = $row.find('input[name="province"]').val();
            var cheeseName = $row.find('input[name="cheesename"]').val();
            var manufacturer = $row.find('input[name="manufacturer"]').val();
            var milkytype = $row.find('input[name="milkytype"]').val();
            var fatprcnt = $row.find('input[name="fatpercent"]').val();

            /* Hide columns*/
            var moisture = $row.find('input[name="moisture"]').val();
            var milktreatment = $row.find('input[name="milktreatment"]').val();
            var process = $row.find('input[name="Manufacturingtyp"]').val();
            var ripening = $row.find('input[name="ripening"]').val();
            var rindtype = $row.find('input[name="rindtype"]').val();
            var organic = $row.find('input[name="organic"]').val();
            var website = $row.find('input[name="website"]').val();

            var particularities = $row.find('input[name="particularities"]').val();
            var flavour = $row.find('input[name="flavour"]').val();
            var characteristics = $row.find('input[name="characteristics"]').val();
            var categoryType = $row.find('input[name="categoryType"]').val();

            /* DATA TO */
            /* Modal Title*/
            $("#mod-rowNum").text(row_num);
            $("#mod-cheeseName").text(cheeseName);
            $("#mod-province").text(province);

            /* Modal Body*/

            $("#mod-milkytype").text(milkytype);
            $("#mod-milkytreat").text(milktreatment);
            $("#mod-fatpercent").text(fatprcnt);
            $("#mod-moisture").text(moisture);
            $("#mod-mantype").text(process);
            $("#mod-ripening").text(ripening);
            $("#mod-rindtype").text(rindtype);
            $("#mod-organic").text(organic);

            $("#mod-particularities").text(particularities);
            $("#mod-flavour").text(flavour);
            $("#mod-characteristics").text(characteristics);
            $("#mod-categoryType").text(categoryType);

            $("#mod-manufacturer").text(manufacturer);
            $("#mod-website").text(website);
            $("#websitelink").attr("href", website);


        });
    });
}