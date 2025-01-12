import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router";
import { Home } from "./pages/home/home";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route index path="/login" element={<Home />} />
          {/* <Route path="/hall" element={<Hall />} /> */}
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
