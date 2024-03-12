import React, { useState } from 'react';

export const PhysicalInfoForm = () => {
  const [age, setAge] = useState('');
  const [height, setHeight] = useState('');
  const [heightUnit, setHeightUnit] = useState('cm');
  const [weight, setWeight] = useState('');
  const [weightUnit, setWeightUnit] = useState('kg');
  const [activityLevel, setActivityLevel] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form submitted:', { age, height, weight, activityLevel });
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col">
    <label>
      Age:
      <input
        type="number"
        value={age}
        onChange={(e) => setAge(e.target.value)}
        required
      />
    </label>
    <br />
    <label>
      Height:
      <input
        type="number"
        value={height}
        onChange={(e) => setHeight(e.target.value)}
        required
      />
      <select value={heightUnit} onChange={(e) => setHeightUnit(e.target.value)}>
        <option value="cm">cm</option>
        <option value="feet">feet</option>
      </select>
    </label>
    <br />
    <label>
      Weight:
      <input
        type="number"
        value={weight}
        onChange={(e) => setWeight(e.target.value)}
        required
      />
      <select value={weightUnit} onChange={(e) => setWeightUnit(e.target.value)}>
        <option value="kg">kg</option>
        <option value="lb">lb</option>
      </select>
    </label>
    <br />
    <label>
      Physical Activity Level:
      <select
        value={activityLevel}
        onChange={(e) => setActivityLevel(e.target.value)}
        required
      >
        <option value="">Select...</option>
        <option value="sedentary">Sedentary</option>
        <option value="lightly_active">Lightly Active</option>
        <option value="moderately_active">Moderately Active</option>
        <option value="very_active">Very Active</option>
        <option value="super_active">Super Active</option>
      </select>
    </label>
    <br />
    <button type="submit">Submit</button>
  </form>
  );
};
