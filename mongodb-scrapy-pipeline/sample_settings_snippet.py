ITEM_PIPELINES = {
   'your_project.pipelines.MongodbPipeline': 300,
   'your_project.pipelines.SQLitePipeline': 400,
   'your_project.pipelines.NewAction': 500,
}
# This code snippet configures the item pipelines for a Scrapy project.
# It specifies the order in which the pipelines will be executed, with lower numbers indicating higher priority