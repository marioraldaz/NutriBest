import React, { useState, useEffect, useContext } from "react";
import { useParams, Navigate } from "react-router-dom";
import { GrayButton } from "../../components/Buttons/GrayButton";
import { RecipeNutrition } from "../../components/Recipes/RecipeNutrition";
import { useSelector, useDispatch } from "react-redux";
import AuthContext from "../../context/AuthContext";
import { NavigationButton } from "../../components/Buttons/NavigationButton";
import { CardsList } from "../../components/Lists/CardsList";
import { Loading } from "../../components/variety/loading";
export function RecipePage() {
  const { id } = useParams();
  const [recipe, setRecipe] = useState(null);
  const [showNutrition, setShowNutrition] = useState(false);
  const [showInstructions, setShowInstructions] = useState(false);
  const [showIngredients, setShowIngredients] = useState(false);
  const [saved, setSaved] = useState(false);
  const [recipeIngredients, setRecipeIngredients] = useState([]);
  const {
    saveRecipe,
    savedRecipes,
    unSaveRecipe,
    setSavedRecipes,
    getRecipe,
    getIngredient,
    setCurrentRecipe,
    currentRecipe,
  } = useContext(AuthContext);

  const recipes = useSelector((state) => state.recipes.recipes);
  const ingredients = useSelector((state) => state.ingredients.ingredients);

  const dispatch = useDispatch();

  useEffect(() => {
    const fetchRecipe = async () => {
      const searched = await getRecipe(id, recipes, dispatch);
      console.log(searched);
      setRecipe(searched);
      savedRecipes.map((savedRecipe) => {
        if (String(savedRecipe.id) === id) {
          setSaved(true);
        }
      });
      const foundIngredientsPromises = await recipe.extendedIngredients?.map(
        async (ing) => {
          return await getIngredient(ing.id, ingredients, dispatch); // Use await to wait for the promise to resolve
        }
      );
      // Use Promise.all to wait for all promises to resolve
      Promise.all(foundIngredientsPromises).then((resolvedIngredients) => {
        setRecipeIngredients(resolvedIngredients); // Log the number of resolved ingredients
        // Process the resolved ingredients here
      });
    };
    fetchRecipe();
  }, [id, savedRecipes, setRecipeIngredients]);

  const toggleNutrition = () => {
    setShowNutrition(!showNutrition);
  };

  const toggleInstructions = () => {
    setShowInstructions(!showInstructions);
  };

  const toggleIngredients = () => {
    setShowIngredients(!showIngredients);
  };
  if (!recipe) {
    return <Loading />;
  }
  return (
    <div className="flex flex-wrap flex-grow p-8 rounded-xl gap-8 min-h-[80vh]">
      <h1 className="w-full gradient-text text-center text-3xl mb-8">
        {recipe.title}{" "}
      </h1>
      <div className="w-full flex flex-wrap gap-8">
        {/*first row*/}
        <img
          src={recipe.image}
          alt={recipe.title}
          className="w-[700px] h-[400px] rounded-lg border"
        />
        <div className="flex flex-col gap-4 w-[200px]">
          <h2>Likes: {recipe.aggregateLikes || "No likes"}</h2>
          <div className="text-white">
            Cooking Minutes:{" "}
            {recipe.cookingMinutes == -1
              ? "Not Specified"
              : recipe.cookingMinutes}
            {recipe.cookingMinutes || "Not specified"}
          </div>
          <div>Gluten Free: {recipe.glutenFree ? "Yes" : "No"}</div>
          <div>Dairy Free: {recipe.dairyFree ? "Yes" : "No"}</div>
        </div>
        <div
          className="ml-auto w-[750px] bg-neutral-800 p-4 rounded-lg justify-center items-center"
          dangerouslySetInnerHTML={{ __html: recipe.summary }}
        />
      </div>
      <div className="w-full flex gap-8">
        {/*second row*/}
        <div className="h-[60px] flex flex-wrap  gap-4">
          {!saved && (
            <div className="w-[200px]">
              <GrayButton
                onClick={() => {
                  saveRecipe(recipe.id);
                  setSaved(true);
                  setSavedRecipes([...savedRecipes, recipe]);
                }}
              >
                Save Recipe
              </GrayButton>
            </div>
          )}
          {saved && (
            <div className="w-[200px]">
              <GrayButton
                onClick={() => {
                  unSaveRecipe(recipe.id);
                  setSaved(false);
                  setSavedRecipes(
                    savedRecipes.filter(
                      (savedRecipe) => savedRecipe.id !== recipe.id
                    )
                  );
                }}
              >
                Unsave Recipe
              </GrayButton>
            </div>
          )}
          <div className="w-[600px] flex h-[60px] items-center">
            <NavigationButton
              link={"/FoodIntake/" + recipe.spoonacular_id}
              text={"Add To Daily"}
            />
          </div>
          <div className="w-[200px]">
            <GrayButton onClick={toggleNutrition}>
              {!showNutrition ? "Show Nutrition" : "Hide Nutrition"}
            </GrayButton>
          </div>

          <div className="w-[200px]">
            <GrayButton onClick={toggleInstructions}>
              {!showInstructions ? "Show Instructions" : "Hide Instructions"}
            </GrayButton>
          </div>

          <div className="w-[200px] ">
            <GrayButton onClick={toggleIngredients}>
              {!showIngredients ? "Show Ingredients" : "Hide Ingredients"}
            </GrayButton>
          </div>
        </div>

        <div className="border p-2 rounded-lg w-[200px]">
          <h2 className="mb-8">Compatible Diets </h2>
          <ul className="flex overflow-auto">
            {recipe.diets.map((diet) => (
              <li
                key={diet}
                className="flex flex-row border p-2 h-[70px] w-[100px] text-center items-center"
              >
                {diet}
              </li>
            ))}
            {recipe.diets.length == 0 && (
              <h3 className="text-2xl">No Compatible Diets Were Saved</h3>
            )}
          </ul>
        </div>
      </div>
      <div className="w-full flex flex-col gap-12">
        {showIngredients && recipe.extendedIngredients?.length > 0 && (
          <div className="h-[400px]  flex flex-row overflow-x-auto overflow-y-hidden w-full">
            <CardsList products={recipeIngredients} />
          </div>
        )}
        {showNutrition && typeof recipe.nutrition === "object" && (
          <>
            <RecipeNutrition recipe={recipe} />
          </>
        )}
        {showNutrition && typeof nutrition !== "object" && (
          <h3 className="text-red-600">Recipe has no nutrition logged :C</h3>
        )}

        {showInstructions && (
          <div className="">
            {recipe.instructions.length > 0 && (
              <div className="flex flex-col">
                <h2 className="text-2xl mb-2">Instructions:</h2>
                <div
                  dangerouslySetInnerHTML={{ __html: recipe.instructions }}
                />
              </div>
            )}
            <ol className="list-decimal">
              {recipe.analyzedInstructions[0]?.steps.map(
                (instruction, index) => (
                  <li
                    key={index}
                    className="flex flex-row gap-4 items-center p-4 border-b border-gray-500 border-b-0.5 "
                  >
                    {index + ". " + instruction.step}
                  </li>
                )
              )}
            </ol>
          </div>
        )}
      </div>
    </div>
  );
}
