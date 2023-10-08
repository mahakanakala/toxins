'use client';
import React, { useState } from 'react';
import axios from 'axios';
import styles from '../page.module.css';

interface SelectedOptions {
  am: boolean;
  pm: boolean;
  oily: boolean;
  normal: boolean;
  combination: boolean;
  dry: boolean;
  under50: boolean;
  under70: boolean;
  under100: boolean;
}

const SkincareRecommendation: React.FC = () => {
  const [recommendedProduct, setRecommendedProduct] = useState<any>(null);
  const [selectedOptions, setSelectedOptions] = useState<SelectedOptions>({
    am: false,
    pm: false,
    oily: false,
    normal: false,
    combination: false,
    dry: false,
    under50: false,
    under70: false,
    under100: false,
  });

  // Function to handle option selection
  const handleOptionClick = (key: keyof SelectedOptions) => {
    setSelectedOptions((prevOptions) => ({
      ...prevOptions,
      [key]: !prevOptions[key],
    }));

    
  };

  return (
    <div className={styles.quizContainer}>
      <div className={styles.questionWrapper}>
        <div className={styles.question1Img}>
          <div className={styles.question1}>
            <h1 className={styles.mainQuestion}>Build a routine! <br /> </h1>
            <h4 className={styles.quizDescription}>Build a skincare routine with clean products</h4>
          </div>
          <div className={styles.question1Options}>
            <ul className={styles.quizOptions}>
              <li>
                <button
                  className={styles.formButton}
                  type="button"
                  title="AM"
                  placeholder="AM"
                  onClick={() => handleOptionClick('am')}
                >
                </button>
                <h4 className={styles.quizOptionText}>AM</h4>
              </li>
              <li >
                <button
                  className={styles.formButton}
                  type="button"
                  title="PM"
                  onClick={() => handleOptionClick("pm")}
                >
                </button>
                <h4 className={styles.quizOptionText}>PM</h4>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div className={styles.question2Wrapper}>
        <div className={styles.question2Img}>
          <div className={styles.question2}>
            <h1 className={styles.mainQuestion} >Skin Type</h1>
          </div>
        </div>
        <div className={styles.question2Options}>
          <ul className={styles.quizOptions}>
            <li>
              <button
                className={styles.formButton}
                type="button"
                title="Oily"
                onClick={()=> handleOptionClick("oily")}
              >
              </button>
              <h4 className={styles.quizOptionText}>Oily</h4>
            </li>
            <li>
              <button
                className={styles.formButton}
                type="button"
                title="Normal"
                onClick={() => handleOptionClick("normal")}>
              </button>
              <h4 className={styles.quizOptionText}>Normal</h4>
            </li>
            <li>
              <button
                className={styles.formButton}
                type="button"
                title="Combination"
                onClick={() => handleOptionClick("combination")}
              >
              </button>
              <h4>Combination</h4>
            </li>
            <li>
              <button
                className={styles.formButton}
                type="button"
                title="Dry"
                onClick={() => handleOptionClick("dry")}>
              </button>
              <h4 className={styles.quizOptionText}>Dry</h4>
            </li>
          </ul>
        </div>

      </div>
      <div className={styles.question3Wrapper}>
        <div className={styles.question3Img}>
          <div className={styles.question3}>
            <h1 className={styles.mainQuestion}>Price Range</h1>
            <div className={styles.question3Options}>
              <ul className={styles.quizOptions}>
                <li>
                  <button
                    className={styles.formButton}
                    type="button"
                    title="Under $50"
                    onClick={() => handleOptionClick("under50")}>
                  </button>
                  <h4 className={styles.quizOptionText}>Under $50</h4>
                </li>
                <li>
                  <button
                    className={styles.formButton}
                    type="button"
                    title="Under $70"
                    onClick={() => handleOptionClick("under70")}>
                  </button>
                  <h4>Under $70</h4>
                </li>
                <li>
                  <button
                    className={styles.formButton}
                    type="button"
                    title="Under $100"
                    onClick={() => handleOptionClick("under100")}>
                  </button>
                  <h4>Under $100</h4>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <button
        className={styles.submitBtn}
        // onClick={handleRecommendation}
      >Submit</button>
      {recommendedProduct && (
        <div className={styles.recommendedProduct}>
          <h2>Recommended Product</h2>
          <p>Name: {recommendedProduct.Name}</p>
          <p>Brand: {recommendedProduct.Brand}</p>

        </div>
      )}
    </div>
  );
};

export default SkincareRecommendation;
