import { BrowserRouter, Route, Routes } from "react-router";
import { Home } from "./pages/home/home";
import { InternationalGalleryHub } from "./pages/InternationalGalleryHub/InternationalGalleryHub";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route index path="/login" element={<Home />} />
          {/* <Route path="/hall" element={<Hall />} /> */}
          <Route
            path="/galeria-internacional"
            element={<InternationalGalleryHub />}
          />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
