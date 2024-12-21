import { useState, useEffect } from "react";
import api from "../api";

function Home() {
  const [notes, setNotes] = useState([]);
  const [content, setContent] = useState("");
  const [title, setTitle] = useState("");

  useEffect(() => {
    fetchNotes();
  }, []);

  const fetchNotes = async () => {
    try {
      const res = await api.get("/api/notes/");
      console.log(res.data);
      setNotes(res.data);
    } catch (error) {
      console.error(error);
    }
  };

  const deleteNote = async (id) => {
    try {
      const res = await api.delete(`/api/notes/delete/${id}/`);
      console.log(res.data);
      alert("Note deleted successfully");
      setNotes(notes.filter((note) => note.id !== id));
    } catch (error) {
      console.error(error);
    }
  };

  const createNote = async () => {
    try {
      const res = await api.post("/api/notes/create/", { title, content });
      console.log(res.data);
      alert("Note created successfully");
      setNotes([...notes, res.data]);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Home</h1>
    </div>
  );
}

export default Home;
