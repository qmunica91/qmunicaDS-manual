<?php

$sourceDir = 'source/es';
$configFile = 'visibility.json';

// Helper function to recursively find .md files
function getMarkdownFiles($dir)
{
    $results = [];
    $files = scandir($dir);

    foreach ($files as $value) {
        $path = realpath($dir . DIRECTORY_SEPARATOR . $value);
        if (!is_dir($path)) {
            if (pathinfo($path, PATHINFO_EXTENSION) === 'md') {
                $results[] = $value; // Store filename only
            }
        }
    }
    return $results;
}

// 1. Load existing config or create empty
$config = [];
if (file_exists($configFile)) {
    $config = json_decode(file_get_contents($configFile), true);
    if (!is_array($config)) {
        $config = [];
    }
}

// 2. Load Navigation Structure
$navBarFile = $sourceDir . '/toc/nav_bar.json';
$orderedFiles = [];

if (file_exists($navBarFile)) {
    $navBar = json_decode(file_get_contents($navBarFile), true);
    if (is_array($navBar)) {
        foreach ($navBar as $item) {
            // Add the main link if it is a local file
            if (isset($item['href']) && strpos($item['href'], '.html') !== false) {
                $file = str_replace('.html', '.md', $item['href']);
                if (!in_array($file, $orderedFiles)) {
                    // Add Section Header for Readability
                    $parentInfo = " [PARENT: $file]";
                    $headerKey = "========= " . strtoupper($item['title']) . "$parentInfo ========= ";
                    if (!in_array($headerKey, $orderedFiles)) {
                        $orderedFiles[] = $headerKey;
                    }
                    $orderedFiles[] = $file;
                }
            } else if (isset($item['title'])) {
                // Even if main link isn't local, we want a header for the TOC items
                $headerKey = "========= " . strtoupper($item['title']) . " =========";
                if (!in_array($headerKey, $orderedFiles)) {
                    $orderedFiles[] = $headerKey;
                }
            }

            // Process TOCs
            if (isset($item['containsToc'])) {
                foreach ($item['containsToc'] as $tocName) {
                    $tocFile = $sourceDir . '/toc/' . $tocName . '.md';
                    if (file_exists($tocFile)) {
                        $tocContent = file_get_contents($tocFile);
                        preg_match_all('/\((.*?\.html)\)/', $tocContent, $matches);
                        if (isset($matches[1])) {
                            foreach ($matches[1] as $link) {
                                $file = str_replace('.html', '.md', $link);
                                if (!in_array($file, $orderedFiles)) {
                                    $orderedFiles[] = $file;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

// 3. Scan for ALL files
$allFiles = getMarkdownFiles($sourceDir);
$newFilesCount = 0;
$finalConfig = [];

// 4. Build Final Config in Order
// First, add ordered files
foreach ($orderedFiles as $file) {
    // Check if it's a separator OR a valid file
    if (strpos($file, '=========') === 0 || in_array($file, $allFiles)) {
        $finalConfig[$file] = $config[$file] ?? ($file[0] === '=' ? '----------------' : 'public');
    }
}

// Second, add remaining files (orphans)
foreach ($allFiles as $file) {
    if (!isset($finalConfig[$file])) {
        $finalConfig[$file] = $config[$file] ?? 'public';
        $newFilesCount++;
    }
}

// 5. Save config
file_put_contents($configFile, json_encode($finalConfig, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES));

echo "Scanned content in $sourceDir" . PHP_EOL;
echo "Found " . count($allFiles) . " markdown files." . PHP_EOL;
echo "Reordered config based on navigation." . PHP_EOL;
echo "Added $newFilesCount new (uncategorized) files to $configFile." . PHP_EOL;
