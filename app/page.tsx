"use client";
import styles from "./page.module.css";
import AnimatedArrow from "./components/AnimatedArrow";
import Scrolling from "./components/Scrolling";
import TypingEffect from "./components/TypingEffect";
import { BiSearch } from "react-icons/bi";
import Scanner from './components/scanner';
import React, { useState } from 'react';
import { Html5QrcodeScanner, Html5QrcodeScanType } from 'html5-qrcode';

interface QrCodeConfig {
  fps: number;
  qrbox: { width: 250; height: 250 };
  rememberLastUsedCamera: boolean;
  supportedScanTypes: Html5QrcodeScanType[];
}

export default function Home() {
  const typingText = "The Ordinary Hyaluronic Acid";
  const [qrCodeData, setQrCodeData] = useState<string>("");
  let html5QrcodeScanner: Html5QrcodeScanner;

  const handleQrCodeScan = (decodedText: string) => {
    // Handle the QR code scan result here
    setQrCodeData(decodedText);
  };

  const config: QrCodeConfig = {
    fps: 10,
    qrbox: { width: 250, height: 250 },
    rememberLastUsedCamera: true,
    supportedScanTypes: [Html5QrcodeScanType.SCAN_TYPE_CAMERA],
  };

  return (
    <main className={styles.wrapperMain}>
      <div className={styles.landingHeaderBox}>
        <h1 className={styles.webtitle}>What's in your Skincare?</h1>
        <AnimatedArrow />
      </div>
      <div className={styles.headerBox}>
        <h1 className={styles.searchwebtitle}>Type your product here</h1>
        <div className={styles.safeSearchContainer}>
        <TypingEffect text={typingText} />
        <div className={styles.searchContainer}>
          <button title="submit" className={styles.safeSubmitBtn} type="submit">
            <BiSearch />
          </button>
        </div>
        <Scanner qrCodeSuccessCallback={handleQrCodeScan} />
      </div>
        <div className={styles.qrCodeBox}>
        <h2 className={styles.scanMessage}>Scanned QR Code Data: </h2>
        <div className={styles.qrCodeData}>{qrCodeData}</div>
      </div>
        <p className={styles.safeDisclaimer}>
          This dataset contains a limited number of products available. If the product you're looking for is not available, we apologize.
        </p>
      </div>
      <div className={styles.learnMoreLink}>
        <a title='project' href='/about' target="_self" rel="noopener noreferrer">
          <h2 className={styles.learnMoreText}>Click to</h2>
          <h2 className={styles.learnMoreText2}> Learn more.</h2>
        </a>
      </div>
      <Scrolling />
    </main>
  );
}
