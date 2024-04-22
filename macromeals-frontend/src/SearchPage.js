import React, { useState } from 'react';
import axios from 'axios';
import './styles.css'

function SearchPage() {
  const [caloriesOperator, setCaloriesOperator] = useState('<');
  const [caloriesValue, setCaloriesValue] = useState('');
  const [fatOperator, setFatOperator] = useState('<');
  const [fatValue, setFatValue] = useState('');
  const [saturatedFatOperator, setSaturatedFatOperator] = useState('<');
  const [saturatedFatValue, setSaturatedFatValue] = useState('');
  const [cholesterolOperator, setCholesterolOperator] = useState('<');
  const [cholesterolValue, setCholesterolValue] = useState('');
  const [proteinOperator, setProteinOperator] = useState('<');
  const [proteinValue, setProteinValue] = useState('');
  const [carbohydratesOperator, setCarbohydratesOperator] = useState('<');
  const [carbohydratesValue, setCarbohydratesValue] = useState('');
  const [fiberOperator, setFiberOperator] = useState('<');
  const [fiberValue, setFiberValue] = useState('');
  const [sugarOperator, setSugarOperator] = useState('<');
  const [sugarValue, setSugarValue] = useState('');
  const [caffeineOperator, setCaffeineOperator] = useState('<');
  const [caffeineValue, setCaffeineValue] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  const handleSearch = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:5000/search?caloriesOperator=${caloriesOperator}&caloriesValue=${caloriesValue}&fatOperator=${fatOperator}&fatValue=${fatValue}&saturatedFatOperator=${saturatedFatOperator}&saturatedFatValue=${saturatedFatValue}&cholesterolOperator=${cholesterolOperator}&cholesterolValue=${cholesterolValue}&proteinOperator=${proteinOperator}&proteinValue=${proteinValue}&carbohydratesOperator=${carbohydratesOperator}&carbohydratesValue=${carbohydratesValue}&fiberOperator=${fiberOperator}&fiberValue=${fiberValue}&sugarOperator=${sugarOperator}&sugarValue=${sugarValue}&caffeineOperator=${caffeineOperator}&caffeineValue=${caffeineValue}`);    
      setSearchResults(response.data);
    } catch (error) {
      console.error('Error fetching search results:', error);
    }
  };

  return (
    <div className="search-container">
      <div className="form-group">
        <label htmlFor="calories">Calories:</label>
        <select id="calories" value={caloriesOperator} onChange={(e) => setCaloriesOperator(e.target.value)}>
          <option value="<">Less Than</option>
          <option value="=">Equal To</option>
          <option value=">">Greater Than</option>
        </select>
        <input
          type="number"
          placeholder="Enter calories value"
          value={caloriesValue}
          onChange={(e) => setCaloriesValue(e.target.value)}
        />
      </div>
      <div className="form-group">
        <label htmlFor="fat">Fat:</label>
        <select id="fat" value={fatOperator} onChange={(e) => setFatOperator(e.target.value)}>
          <option value="<">Less Than</option>
          <option value="=">Equal To</option>
          <option value=">">Greater Than</option>
        </select>
        <input
          type="number"
          placeholder="Enter fat value"
          value={fatValue}
          onChange={(e) => setFatValue(e.target.value)}
        />
      </div>
      <div className="form-group">
        <label htmlFor="saturated-fat">Saturated Fat:</label>
        <select id="saturated-fat" value={saturatedFatOperator} onChange={(e) => setSaturatedFatOperator(e.target.value)}>
          <option value="<">Less Than</option>
          <option value="=">Equal To</option>
          <option value=">">Greater Than</option>
        </select>
        <input
          type="number"
          placeholder="Enter saturated fat value"
          value={saturatedFatValue}
          onChange={(e) => setSaturatedFatValue(e.target.value)}
        />
      </div>
      <div className="form-group">
        <label htmlFor="cholesterol">Cholesterol:</label>
        <select id="cholesterol" value={cholesterolOperator} onChange={(e) => setCholesterolOperator(e.target.value)}>
          <option value="<">Less Than</option>
          <option value="=">Equal To</option>
          <option value=">">Greater Than</option>
        </select>
        <input
          type="number"
          placeholder="Enter cholesterol value"
          value={cholesterolValue}
          onChange={(e) => setCholesterolValue(e.target.value)}
        />
      </div>
      <div className="form-group">
        <label htmlFor="protein">Protein:</label>
        <select id="protein" value={proteinOperator} onChange={(e) => setProteinOperator(e.target.value)}>
          <option value="<">Less Than</option>
          <option value="=">Equal To</option>
          <option value=">">Greater Than</option>
        </select>
        <input
          type="number"
          placeholder="Enter protein value"
          value={proteinValue}
          onChange={(e) => setProteinValue(e.target.value)}
        />
      </div>
      <div className="form-group">
        <label htmlFor="carbohydrates">Carbohydrates:</label>
        <select id="carbohydrates" value={carbohydratesOperator} onChange={(e) => setCarbohydratesOperator(e.target.value)}>
          <option value="<">Less Than</option>
          <option value="=">Equal To</option>
          <option value=">">Greater Than</option>
        </select>
        <input
          type="number"
          placeholder="Enter carbohydrates value"
          value={carbohydratesValue}
          onChange={(e) => setCarbohydratesValue(e.target.value)}
        />
      </div>
      <div className="form-group">
        <label htmlFor="fiber">Fiber:</label>
        <select id="fiber" value={fiberOperator} onChange={(e) => setFiberOperator(e.target.value)}>
          <option value="<">Less Than</option>
          <option value="=">Equal To</option>
          <option value=">">Greater Than</option>
        </select>
        <input
          type="number"
          placeholder="Enter fiber value"
          value={fiberValue}
          onChange={(e) => setFiberValue(e.target.value)}
        />
      </div>
      <div className="form-group">
        <label htmlFor="sugar">Sugar:</label>
        <select id="sugar" value={sugarOperator} onChange={(e) => setSugarOperator(e.target.value)}>
          <option value="<">Less Than</option>
          <option value="=">Equal To</option>
          <option value=">">Greater Than</option>
        </select>
        <input
          type="number"
          placeholder="Enter sugar value"
          value={sugarValue}
          onChange={(e) => setSugarValue(e.target.value)}
        />
      </div>
      <div className="form-group">
        <label htmlFor="caffeine">Caffeine:</label>
        <select id="caffeine" value={caffeineOperator} onChange={(e) => setCaffeineOperator(e.target.value)}>
          <option value="<">Less Than</option>
          <option value="=">Equal To</option>
          <option value=">">Greater Than</option>
        </select>
        <input
          type="number"
          placeholder="Enter caffeine value"
          value={caffeineValue}
          onChange={(e) => setCaffeineValue(e.target.value)}
        />
      </div>
      <button onClick={handleSearch}>Search</button>
      <div className="search-results">
        <ul>
        {searchResults.map((result, index) => (
            <li key={index}>
              <div>
                <p>Name: {result.name}</p>
                <p>Ingredients: {result.ingredients}</p>
                <p>Directions: {result.directions}</p>
                <p>Calories: {result.calories}</p>
                <p>Fat (g): {result.fat}</p>
                <p>Saturated Fat (g): {result.saturated_fat}</p>
                <p>Cholesterol (mg): {result.cholesterol}</p>
                <p>Protein (g): {result.protein}</p>
                <p>Carbohydrates (g): {result.carbohydrates}</p>
                <p>Fiber (g): {result.fiber}</p>
                <p>Sugar (g): {result.sugar}</p>
                <p>Caffeine (mg): {result.caffeine}</p>
                <p>Quantity (est. cups): {result.quantity}</p>
                <p>Link: {result.link}</p>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default SearchPage;

