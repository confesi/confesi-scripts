mongosh
use db
db.comments.updateOne({ _id: ObjectId("63f1f98afa1a3df58f7797d1") }, { $set: { votes_up: 13 } })
db.comments.updateOne({ _id: ObjectId("63f1f992fa1a3df58f7797d2") }, { $set: { votes_up: 12 } })
db.comments.updateOne({ _id: ObjectId("63f1f994fa1a3df58f7797d3") }, { $set: { votes_up: 12 } })
db.comments.updateOne({ _id: ObjectId("63f1f997fa1a3df58f7797d4") }, { $set: { votes_up: 15 } })
db.comments.updateOne({ _id: ObjectId("63f1f999fa1a3df58f7797d5") }, { $set: { votes_up: 7 } })
db.comments.updateOne({ _id: ObjectId("63f1f99cfa1a3df58f7797d6") }, { $set: { votes_up: 2 } })
db.comments.updateOne({ _id: ObjectId("63f1f99efa1a3df58f7797d7") }, { $set: { votes_up: 0 } })
db.comments.updateOne({ _id: ObjectId("63f1f9a0fa1a3df58f7797d8") }, { $set: { votes_up: 17 } })
db.comments.updateOne({ _id: ObjectId("63f1f9a3fa1a3df58f7797d9") }, { $set: { votes_up: 5 } })
db.comments.updateOne({ _id: ObjectId("63f1f9a6fa1a3df58f7797da") }, { $set: { votes_up: 8 } })