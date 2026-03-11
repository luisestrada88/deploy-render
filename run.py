import os
from typing import List

import numpy as np
import tensorflow as tf
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class InputPayload(BaseModel):
    vector: List[float] = Field(..., min_length=3, max_length=3)


def build_and_train_autoencoder() -> tf.keras.Model:
    x = np.array([[1.0, 0.0, 1.0]], dtype=np.float32)

    model = tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(3,)),
            tf.keras.layers.Dense(2, activation="sigmoid"),
            tf.keras.layers.Dense(3, activation="sigmoid"),
        ]
    )

    model.compile(
        optimizer=tf.keras.optimizers.SGD(learning_rate=0.5),
        loss="mse",
    )

    model.fit(x, x, epochs=200, verbose=0)
    return model


app = FastAPI(title="Autoencoder API", version="1.0.0")
model = None


def get_model() -> tf.keras.Model:
    global model
    if model is None:
        model = build_and_train_autoencoder()
    return model


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/")
def root() -> dict:
    return {
        "message": "Autoencoder API running",
        "endpoints": ["/health", "/reconstruct", "/docs"],
    }


@app.post("/reconstruct")
def reconstruct(payload: InputPayload) -> dict:
    try:
        current_model = get_model()
        vector = np.array([payload.vector], dtype=np.float32)
        prediction = current_model.predict(vector, verbose=0)[0].tolist()
        return {
            "input": payload.vector,
            "reconstruction": prediction,
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("run:app", host="0.0.0.0", port=port)