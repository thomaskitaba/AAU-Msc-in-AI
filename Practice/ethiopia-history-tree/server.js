
import express from "express";
import cors from "cors";


// Sample city adjacency data
const sampleData = [
  { city: "Addis Ababa", neighbors: ["Adama", "Debre Zeit"] },
  { city: "Adama", neighbors: ["Addis Ababa", "Bishoftu"] },
  { city: "Debre Zeit", neighbors: ["Addis Ababa", "Modjo"] },
  { city: "Modjo", neighbors: ["Debre Zeit", "Adama"] }
];

const importantPersonsHistory = {"name": {}, "name2": {}}
const zemeneMesafent = [  "ትልቁ ራስ አሊ": {}, "አሊጋዝ", "ራስ አስራት | ራስ  ኃይለ ገብርኤል": {}, "ራስ ጉግሳ | ጉግሳ ": {}, "ራስ ይማም ": {}, "ራስ ማሬ ": {}, "ራስ ዶሪ": {}, "ትንሹ አሊ": {}]
const historyKingsData = [
  {"ethiopianKings": ["ልብነ ድንግል", "ገላውዴዎስ", "ሚናስ", "ሰርፀድንግል", "ሚናስ ", "  ያዕቆብ", "ዘድንግል", " ሱስንዮስ", "ፋስል", "ዮሐንስ ", "አድያም ሰገድ ኢያሱ", "ረጉም ተክለሀይማኖት", " ቴዎፍሎስ ", "ዮስጦስ ", " ዳዊት", " በካፋ ",  " ቋረኛው ኢያሱ", "ኢዮአስ ", " አንድ እጅ ዮሀንስ", "ተክለ ለሀይማኖት ", "ተክለጊዮርጊስ ", " አፄ ቴዎድሮስ | የቋራው ካሳ ", " ዋግሹም ጎበዜ", " አፄ ዮሀንስ | ዮሀንስ | አጤ ዮሀንስ ", "አጤ ምኒሊክ| አፄ | ምኒሊክ  ", " ሀይለ ስላሴ", " ", "  "]},



  
  {"shewaLeadersKinship": {
    "ልብነ ድንግል": ["ያዕቆብ", "ሚናስ", "ፊቅጦር", "አመተ ጊዮርጊስ", "ሰበነ ጊዮርጊስ", "ወለተ ቅዱሳን", "ታኦዱራ", "ገላውዴዎስ" ],
    
    "ያእቆብ": ["ተዝካረ ቃል"], "ስግወ ቃል": ["ወረደ ቃል"], "ልብሰ ቃል": [""], }
  }, 
  {"gojamLeadersKinship": {}},
  {"gondarLeadersKinship": {}}
]

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware setup
app.use(express.json()); //This middleware parses incoming JSON payloads and makes the data available in req.body.
app.use(cors());

// Define your route directly in this file
app.get('/api/graphs/sample', (req, res) => {
  res.json(sampleData);
});
app.get('/', (req, res) => {
    res.json(sampleData)
})
// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
