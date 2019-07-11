queue()
  .defer(d3.json, "/data_recipes")
  .await(createCharts);

function createCharts(error, data) {
  var recipes = data;

  var ndx = crossfilter(recipes);

  var dimDifficulty = ndx.dimension(dc.pluck("difficulty"));
  var groupDifficulty = dimDifficulty.group();

  dc.pieChart("#difficulty")
    .height(200)
    .useViewBoxResizing(true) //to make the chart responsive
    .externalRadiusPadding(40)
    .dimension(dimDifficulty)
    .group(groupDifficulty)
    .renderLabel(false) //we use the legend instead
    .transitionDuration(1500);

  var dimCategory = ndx.dimension(dc.pluck("category"));
  var groupCategory = dimCategory.group();

  dc.pieChart("#category")
    .height(200)
    .useViewBoxResizing(true) //to make the chart responsive
    .externalRadiusPadding(40)
    .dimension(dimCategory)
    .group(groupCategory)
    .renderLabel(false) //we use the legend instead
    .transitionDuration(1500);

  var dimCuisine = ndx.dimension(dc.pluck("cuisine"));
  var groupCuisine = dimCuisine.group();

  dc.barChart("#cuisine")
    .height(200)
    .useViewBoxResizing(true) //to make the chart responsive
    // .margins({ top: 15, right: 10, bottom: 55, left: 35 })
    .renderHorizontalGridLines(true)
    .dimension(dimCuisine)
    .group(groupCuisine)

    // .title(function (d) {
    //     return 'In ' + d.key + ' the ' + this.layer + ' by day cost: ' + d.value + '€';
    // })
    .ordinalColors(["#006B99", "#0E9E8D", "#F2C44F", "#F4994E", "#E86443"])
    .transitionDuration(1500)
    .x(d3.scale.ordinal())
    .xUnits(dc.units.ordinal)
    .barPadding(0.3)
    .xAxisLabel("Cuisines")
    .yAxisLabel("Number of recipes")
    .yAxis()
    .ticks(6);

  var total = ndx.groupAll().reduce(
    //p keeps track of the changes, v will be input values from the dataset
    //function adder
    function(p, v) {
      p.count++;
      return p;
    },
    //function remover
    function(p, v) {
      p.count--;
      return p;
    },
    //Initialise the Reducer
    function() {
      return { count: 0 };
    }
  );

  dc.numberDisplay("#totalRecipes")
    .formatNumber(d3.format("d"))
    .valueAccessor(function(d) {
      return d.count;
    })
    .group(total);

  var allDimension = ndx.dimension(function(d) {
    return d;
  });

  dc.dataTable("#table")
    .height(300)
    .width(400)
    .useViewBoxResizing(true) //to make the chart responsive
    .dimension(allDimension)
    .group(function(data) {
      return data;
    })
    .size(Infinity)
    .columns([
      {
        label: "Recipe_Name",
        format: function(d) {
          return d.recipe_name;
        }
      },
      {
        label: "Votes",
        format: function(d) {
          return d.upvotes;
        }
      },
      {
        label: "Cuisine",
        format: function(d) {
          return d.cuisine;
        }
      },
      {
        label: "Category",
        format: function(d) {
          return d.category;
        }
      },
      {
        label: "View recipe",
        format: function(d) {
          // get the id value and remove the "
          var keystring = JSON.stringify(d._id["$oid"]).replace(/"/g, "");
          // var key = keystring.replace(/"/g, "");
          // return "how to add this link ?? view_recipe/" + keystring;
          return '<a href="https://www.google.com/"></a>';
        }
      }
    ])
    // .sortBy(d.upvotes)
    .showGroups(false) // this will remove the [object][object] at the top of the rows
    .order(d3.ascending);
  dc.renderAll();
}
