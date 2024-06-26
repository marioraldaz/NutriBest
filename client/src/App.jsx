import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Header } from "./components/Header.jsx";
import { Home } from "./pages/Home.jsx";
import { Ingredients } from "./pages/Ingredients/Ingredients.jsx";
import { Recipes } from "./pages/Recipes/Recipes.jsx";
import { MyBalance } from "./pages/MyBalance/MyBalance.jsx";
import { Footer } from "./components/Footer.jsx";
import { IngredientPage } from "./pages/Ingredients/IngredientPage.jsx";
import { Profile } from "./pages/Profile/Profile.jsx";
import { Login } from "./pages/Profile/Login.jsx";
import { Register } from "./pages/Profile/Register.jsx";
import { RequireAuth } from "./pages/Profile/RequireAuth.jsx";
import { AuthProvider } from "./context/AuthContext.jsx";
import { Provider } from "react-redux";
import { FoodIntake } from "./pages/FoodIntake/FoodIntake.jsx";
import { RecipePage } from "./pages/Recipes/RecipePage.jsx";
import { PersistGate } from "redux-persist/integration/react";
import { store, persistor } from "./redux/store";
import { NutriExpert } from "./pages/NutriExpert/NutriExpert.jsx";
function App() {
  return (
    <Provider store={store}>
      <PersistGate loading={null} persistor={persistor}>
        <BrowserRouter>
          <AuthProvider>
            <div className="bg-black absolute z-[-1] min-h-screen w-full text-white flex flex-col overflow-hidden">
              <Header />
              <div className="flex-1 relative z-[0]">
                <Routes>
                  <Route path="/" element={<Home />} />
                  <Route path="/Ingredients" element={<Ingredients />} />
                  <Route path="/Recipes" element={<Recipes />} />
                  <Route path="/MyBalance" element={<MyBalance />} />
                  <Route path="/Ingredient/:id" element={<IngredientPage />} />
                  <Route path="/login" element={<Login />} />
                  <Route path="/Register" element={<Register />} />
                  <Route path="/Profile" element={<Profile />} />
                  <Route path="/RequireAuth" element={<RequireAuth />} />
                  <Route path="/Recipe/:id" element={<RecipePage />} />
                  <Route path="/FoodIntake/:add" element={<FoodIntake />} />
                  <Route path="/NutriExpert" element={<NutriExpert />} />
                </Routes>
              </div>
              <Footer />
            </div>
          </AuthProvider>
        </BrowserRouter>
      </PersistGate>
    </Provider>
  );
}

export default App;
